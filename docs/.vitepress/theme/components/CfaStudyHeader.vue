<script setup lang="ts">
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'

const { frontmatter } = useData()
const crumbs = computed(() => {
  const study = frontmatter.value.study
  if (!study) return []
  const result = [{ text: 'CFA 2027', link: '/cfa/' }]
  if (study.system) result.push({ text: study.system === 'questions' ? 'Question Bank' : 'Review Course', link: `/cfa/${study.system}/` })
  if (study.category) result.push({ text: study.category, link: study.categoryLink })
  if (study.topic) result.push({ text: study.topic, link: study.topicLink })
  if (study.moduleLink) result.push({ text: study.module, link: study.moduleLink })
  return result
})
</script>

<template>
  <div v-if="frontmatter.study" class="study-header">
    <nav aria-label="Course breadcrumb">
      <template v-for="(crumb, index) in crumbs" :key="crumb.link">
        <span v-if="index" aria-hidden="true">/</span>
        <a :href="withBase(crumb.link)">{{ crumb.text }}</a>
      </template>
    </nav>
    <span v-if="frontmatter.study.step" class="study-position">
      STEP {{ String(frontmatter.study.step).padStart(2, '0') }} / {{ String(frontmatter.study.total).padStart(2, '0') }}
    </span>
    <span v-else class="study-position">{{ frontmatter.study.section }}</span>
  </div>
</template>
