//
// gate.ts —— 站点登录门禁的核心逻辑
//
// 凭证写死：明文密码不进入仓库，只存「用户名:密码:盐」的 SHA-256 摘要。
// 输入格式：`${username}:${password}:${SALT}`
//
// 这是针对「静态站 + 不想被搜索引擎收录」的防护：
//   - 服务端渲染（vitepress build）阶段同样处于未登录态，产物 HTML 里只有登录页，
//     页面正文不会出现在预渲染的静态 HTML 中；
//   - 登录成功后写入 localStorage 会话（180 天），SPA 内导航不再拦截。
//

const SALT = 'wjxblog-vault-2026'
const HASH = '13dccc4e3f371afb42f8a11e18a19cc283c7032d532d6d1d0e3afa6710d3b9e8'
export const STORAGE_KEY = 'wjxblog_gate_v1'
const SESSION_TTL = 180 * 24 * 3600 * 1000 // 180 天

// ── 纯 JS 实现的 SHA-256（已对照 Node crypto 验证一致） ──────────────
const K = [
  0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
  0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
  0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
  0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
  0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
  0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
  0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
  0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

function rotr(x: number, n: number): number {
  return ((x >>> n) | (x << (32 - n))) >>> 0
}

export function sha256(msg: string): string {
  const H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
  const utf8 = new TextEncoder().encode(msg)
  const l = utf8.length
  const total = (((l + 1 + 8) >> 6) + 1) << 6
  const bytes = new Uint8Array(total)
  bytes.set(utf8)
  bytes[l] = 0x80
  const dv = new DataView(bytes.buffer)
  dv.setUint32(total - 8, Math.floor((l * 8) / 0x100000000))
  dv.setUint32(total - 4, (l * 8) >>> 0)
  const w = new Uint32Array(64)
  for (let i = 0; i < total; i += 64) {
    for (let j = 0; j < 16; j++) w[j] = dv.getUint32(i + j * 4)
    for (let j = 16; j < 64; j++) {
      const s0 = rotr(w[j - 15], 7) ^ rotr(w[j - 15], 18) ^ (w[j - 15] >>> 3)
      const s1 = rotr(w[j - 2], 17) ^ rotr(w[j - 2], 19) ^ (w[j - 2] >>> 10)
      w[j] = (w[j - 16] + s0 + w[j - 7] + s1) >>> 0
    }
    let a = H[0], b = H[1], c = H[2], d = H[3], e = H[4], f = H[5], g = H[6], h = H[7]
    for (let j = 0; j < 64; j++) {
      const S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
      const ch = (e & f) ^ (~e & g)
      const t1 = (h + S1 + ch + K[j] + w[j]) >>> 0
      const S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
      const maj = (a & b) ^ (a & c) ^ (b & c)
      const t2 = (S0 + maj) >>> 0
      h = g; g = f; f = e
      e = (d + t1) >>> 0
      d = c; c = b; b = a
      a = (t1 + t2) >>> 0
    }
    H[0] = (H[0] + a) >>> 0; H[1] = (H[1] + b) >>> 0; H[2] = (H[2] + c) >>> 0; H[3] = (H[3] + d) >>> 0
    H[4] = (H[4] + e) >>> 0; H[5] = (H[5] + f) >>> 0; H[6] = (H[6] + g) >>> 0; H[7] = (H[7] + h) >>> 0
  }
  return H.map((x) => x.toString(16).padStart(8, '0')).join('')
}

// ── 会话与校验 ─────────────────────────────────────────────────────

function isDevHost(): boolean {
  return typeof location !== 'undefined' && /^(localhost|127\.0\.0\.1)$/.test(location.hostname)
}

export function hasValidSession(): boolean {
  if (typeof localStorage === 'undefined') return false
  if (isDevHost()) return true // 本地 vitepress dev 免登录，部署站点不受影响
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) return false
    const s = JSON.parse(raw)
    return s?.h === HASH && typeof s.t === 'number' && Date.now() - s.t < SESSION_TTL
  } catch {
    return false
  }
}

export function verifyCredential(username: string, password: string): boolean {
  return sha256(`${username}:${password}:${SALT}`) === HASH
}

export function createSession(): void {
  localStorage.setItem(STORAGE_KEY, JSON.stringify({ h: HASH, t: Date.now() }))
}

// 移除防闪现隐藏（config.mts head 注入：html.gate-hold #app{visibility:hidden}）
export function revealSite(): void {
  document.documentElement.classList.remove('gate-hold')
}
