<script setup lang="ts">
import { useData } from 'vitepress'

const { frontmatter } = useData()
</script>

<template>
  <nav v-if="frontmatter.studyNav" class="study-nav" aria-label="Learning navigation">
    <a v-for="(item, key) in frontmatter.studyNav" :key="key" :href="item.link" :class="`study-nav-${key}`">
      <span>{{ item.label }}</span>
      <strong>{{ item.title }}</strong>
    </a>
  </nav>
</template>
