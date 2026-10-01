<script setup lang="ts">
import { useData } from 'vitepress'

const { frontmatter } = useData()
</script>

<template>
  <div v-if="frontmatter.study" class="study-header">
    <nav aria-label="Course breadcrumb">
      <a href="/cfa/asset-allocation/">Asset Allocation</a>
      <span aria-hidden="true">/</span>
      <a v-if="frontmatter.study.moduleLink" :href="frontmatter.study.moduleLink">{{ frontmatter.study.module }}</a>
      <span v-else>{{ frontmatter.study.section }}</span>
    </nav>
    <span v-if="frontmatter.study.step" class="study-position">
      STEP {{ String(frontmatter.study.step).padStart(2, '0') }} / {{ String(frontmatter.study.total).padStart(2, '0') }}
    </span>
    <span v-else class="study-position">{{ frontmatter.study.section }}</span>
  </div>
</template>
