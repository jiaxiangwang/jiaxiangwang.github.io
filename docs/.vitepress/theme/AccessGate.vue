//
// AccessGate.vue —— 全站登录门禁组件
// 未登录时：遮罩站点内容，仅显示登录卡片；验证通过后放行并挂 SPA 路由守卫。
// 已登录时：整站正常渲染（此组件 render null）。
//
<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { hasValidSession, verifyCredential, createSession, revealSite } from './gate'

const authed = ref<boolean | null>(null) // null = 检查中
const username = ref('')
const password = ref('')
const error = ref('')
const checking = ref(false)

onMounted(() => {
  authed.value = hasValidSession()
  if (authed.value) revealSite()
})

function submit() {
  error.value = ''
  if (!username.value || !password.value) {
    error.value = '请输入用户名和密码'
    return
  }
  checking.value = true
  // 延迟一帧，降低暴力枚举速率（非安全边界，仅增加成本）
  setTimeout(() => {
    if (verifyCredential(username.value, password.value)) {
      createSession()
      authed.value = true
      revealSite()
    } else {
      error.value = '用户名或密码错误'
    }
    checking.value = false
  }, 350)
}

function logout() {
  localStorage.removeItem('wjxblog_gate_v1')
  location.reload()
}
</script>

<template>
  <div v-if="authed === false" class="gate-overlay">
    <div class="gate-card">
      <div class="gate-logo">🔒</div>
      <h1 class="gate-title">Jasper 的个人笔记</h1>
      <p class="gate-sub">私人站点 · 请登录后访问</p>
      <form @submit.prevent="submit">
        <label class="gate-field">
          <span>用户名</span>
          <input v-model="username" type="text" autocomplete="username" spellcheck="false" />
        </label>
        <label class="gate-field">
          <span>密码</span>
          <input v-model="password" type="password" autocomplete="current-password" />
        </label>
        <p v-if="error" class="gate-error">{{ error }}</p>
        <button class="gate-btn" type="submit" :disabled="checking">
          {{ checking ? '验证中…' : '进入' }}
        </button>
      </form>
      <p class="gate-footnote">仅限本人访问 · 未获授权的访问请立即离开</p>
    </div>
  </div>
  <Teleport to="body">
    <button v-if="authed === true" class="gate-logout" title="退出登录" @click="logout">退出</button>
  </Teleport>
</template>

<style scoped>
.gate-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--vp-c-bg);
  padding: 24px;
}

.gate-card {
  width: 100%;
  max-width: 360px;
  padding: 36px 32px 28px;
  border: 1px solid var(--vp-c-border);
  border-radius: 14px;
  background: var(--vp-c-bg-soft);
  text-align: center;
}

.gate-logo { font-size: 34px; line-height: 1; }
.gate-title { margin: 14px 0 4px; font-size: 20px; font-weight: 700; color: var(--vp-c-text-1); }
.gate-sub { margin: 0 0 22px; font-size: 13px; color: var(--vp-c-text-3); }

.gate-field { display: block; text-align: left; margin-bottom: 14px; }
.gate-field span { display: block; font-size: 12px; font-weight: 600; color: var(--vp-c-text-2); margin-bottom: 6px; }
.gate-field input {
  width: 100%;
  box-sizing: border-box;
  padding: 9px 12px;
  font-size: 14px;
  border-radius: 8px;
  border: 1px solid var(--vp-c-border);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  outline: none;
  transition: border-color 0.2s;
}
.gate-field input:focus { border-color: var(--vp-c-brand-1); }

.gate-error { margin: 0 0 10px; font-size: 13px; color: var(--vp-c-danger-1); }

.gate-btn {
  width: 100%;
  padding: 10px 0;
  font-size: 14px;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  background: var(--vp-c-brand-1);
  color: var(--vp-button-brand-text, #fff);
  cursor: pointer;
  transition: opacity 0.2s;
}
.gate-btn:hover { opacity: 0.85; }
.gate-btn:disabled { opacity: 0.5; cursor: wait; }

.gate-footnote { margin: 18px 0 0; font-size: 11px; color: var(--vp-c-text-3); }

.gate-logout {
  position: fixed;
  right: 16px;
  bottom: 16px;
  z-index: 9998;
  padding: 5px 14px;
  font-size: 12px;
  border-radius: 999px;
  border: 1px solid var(--vp-c-border);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  cursor: pointer;
  opacity: 0.55;
  transition: opacity 0.2s;
}
.gate-logout:hover { opacity: 1; }
</style>
