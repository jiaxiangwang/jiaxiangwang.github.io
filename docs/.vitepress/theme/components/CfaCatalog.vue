<script setup lang="ts">
import { computed } from 'vue'
import { withBase } from 'vitepress'
import catalog from '../../../cfa/catalog.json'

type ContentMap = {
  modules: { steps: unknown[] }[]
  questions: { type: string }[]
}

const props = withDefaults(defineProps<{ mode?: 'all' | 'review' | 'questions' }>(), { mode: 'all' })
const contentMaps = import.meta.glob<ContentMap>('../../../cfa/*/content-map.json', { eager: true, import: 'default' })
const groups = computed(() => catalog.groups.map(group => ({
  ...group,
  entries: group.entries.map(entry => {
    const map = contentMaps[`../../../cfa/${entry.id}/content-map.json`]
    return {
      ...entry,
      published: Boolean(map),
      href: `/cfa/${entry.id}/${props.mode === 'questions' ? 'questions/' : ''}`,
      moduleCount: map?.modules.length ?? 0,
      steps: map?.modules.reduce((count, module) => count + module.steps.length, 0) ?? 0,
      mcq: map?.questions.filter(question => question.type === 'MCQ').length ?? 0,
      cr: map?.questions.filter(question => question.type === 'CR').length ?? 0,
    }
  }),
})))
</script>

<template>
  <div v-if="mode === 'all'" class="catalog-modes">
    <a :href="withBase('/cfa/review/')">
      <span class="catalog-eyebrow">知识 → 理解 → 应用</span>
      <strong>Review Course <span aria-hidden="true">→</span></strong>
      <span>按 Learning Map 复习，建立完整的投资决策框架。</span>
    </a>
    <a :href="withBase('/cfa/questions/')">
      <span class="catalog-eyebrow">作答 → 推理 → 知识连接</span>
      <strong>Question Bank <span aria-hidden="true">→</span></strong>
      <span>按 Module 与知识点练习，用题目检验并加深理解。</span>
    </a>
  </div>

  <nav class="catalog-categories" aria-label="Curriculum categories">
    <a v-for="group in groups" :key="group.id" :href="`#${group.id}`">{{ group.name }}</a>
  </nav>

  <section v-for="group in groups" :key="group.id" class="catalog-group" :class="{ 'catalog-module-group': group.unit === 'Learning Module' }" :aria-labelledby="group.id">
    <h2 :id="group.id">{{ group.name }}</h2>
    <p class="catalog-group-note">{{ group.unit === 'Topic' ? '按 Topic 组织共同课程。' : '按仓库 outline 的专属 Learning Modules 组织。' }}</p>

    <div class="catalog-topics">
      <template v-for="entry in group.entries" :key="entry.id">
        <article v-if="entry.published" class="catalog-topic">
          <span class="catalog-eyebrow">{{ group.unit }}</span>
          <h3><a :href="withBase(entry.href)">{{ entry.name }} <span aria-hidden="true">→</span></a></h3>
          <p v-if="mode === 'questions'" class="catalog-stats">{{ entry.mcq }} MCQ · {{ entry.cr }} Constructed Response</p>
          <p v-else class="catalog-stats">{{ entry.moduleCount }} Learning Modules · {{ entry.steps }} Review Steps</p>
          <p v-if="mode === 'all'" class="catalog-topic-actions">
            <a :href="withBase(`/cfa/${entry.id}/`)">Review Course</a>
            <a :href="withBase(`/cfa/${entry.id}/questions/`)">Question Bank · {{ entry.mcq + entry.cr }} 题</a>
          </p>
          <details v-if="mode !== 'questions'" class="catalog-outline">
            <summary>Learning Module 目录</summary>
            <ol>
              <li v-for="module in entry.modules" :key="module.number" :value="module.number">{{ module.name }}</li>
            </ol>
          </details>
        </article>
        <article v-else-if="mode === 'all'" class="catalog-topic catalog-pending">
          <span class="catalog-eyebrow">{{ group.unit }} <span class="catalog-status">未发布</span></span>
          <h3>{{ entry.name }}</h3>
          <details v-if="group.unit === 'Topic'" class="catalog-outline">
            <summary>{{ entry.modules.length }} Learning Modules</summary>
            <ol>
              <li v-for="module in entry.modules" :key="module.number" :value="module.number">{{ module.name }}</li>
            </ol>
          </details>
          <p v-else class="catalog-stats">Module {{ entry.modules[0].number }}</p>
        </article>
      </template>
    </div>
    <p v-if="mode !== 'all' && !group.entries.some(entry => entry.published)" class="catalog-empty">此分类尚无已发布内容。<a :href="withBase(`/cfa/#${group.id}`)">查看 2027 课程目录 →</a></p>
  </section>

  <p v-if="mode !== 'all'" class="catalog-return"><a :href="withBase('/cfa/')">← 学习中心与完整课程目录</a></p>
</template>
