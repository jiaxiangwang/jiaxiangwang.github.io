<script setup lang="ts">
import { computed, ref, watch } from 'vue'

const props = defineProps<{
  id: string
  type?: 'mcq' | 'cr'
  answer?: 'A' | 'B' | 'C'
}>()
const choices = ['A', 'B', 'C'] as const
const selected = ref<'A' | 'B' | 'C' | ''>('')
const submitted = ref(false)
const response = ref('')
const isCr = computed(() => props.type === 'cr')
const correct = computed(() => selected.value === props.answer)
function reset() {
  selected.value = ''
  submitted.value = false
  response.value = ''
}
function reveal() {
  if (isCr.value || selected.value) submitted.value = true
}
watch(() => props.id, reset)
</script>

<template>
  <section class="q-card cfa-interactive" :aria-label="`Question ${id}`">
    <div class="q-stem"><slot name="prompt" /></div>
    <div v-if="isCr" class="cr-input">
      <label :for="`response-${id}`">Your Answer</label>
      <textarea :id="`response-${id}`" v-model="response" rows="5" placeholder="Write a concise CFA response. Use bullets when appropriate." />
    </div>
    <fieldset v-else class="cfa-options" :disabled="submitted">
      <legend>Select one answer</legend>
      <label v-for="choice in choices" :key="choice" :class="{ selected: selected === choice }">
        <input v-model="selected" type="radio" :name="`answer-${id}`" :value="choice" />
        <span class="choice-letter">{{ choice }}.</span>
        <span><slot :name="choice.toLowerCase()" /></span>
      </label>
    </fieldset>
    <div class="cfa-actions">
      <button type="button" :disabled="submitted || (!isCr && !selected)" @click="reveal">
        {{ isCr ? 'Show Answer' : 'Submit Answer' }}
      </button>
      <button v-if="submitted" type="button" class="reset" @click="reset">Try Again</button>
    </div>
    <div v-if="submitted" class="cfa-analysis">
      <div v-if="!isCr" role="status" aria-live="polite" class="cfa-result">
        <strong v-if="correct">✓ Correct</strong>
        <template v-else>
          <strong>✗ Incorrect</strong>
          <p>Your Answer: {{ selected }}<br />Correct Answer: {{ answer }}</p>
        </template>
      </div>
      <slot name="analysis" />
    </div>
  </section>
</template>

<style scoped>
.cfa-options { border: 0; padding: 0; margin: 1rem 0; }
.cfa-options legend, .cr-input label { font-weight: 600; margin-bottom: .5rem; display: block; }
.cfa-options label { display: flex; gap: .65rem; align-items: baseline; padding: .7rem; margin: .4rem 0; border: 1px solid var(--vp-c-divider); border-radius: 7px; cursor: pointer; }
.cfa-options label.selected { border-color: var(--vp-c-brand-1); background: var(--vp-c-brand-soft); }
.cfa-options label span:last-child { flex: 1; }
.choice-letter { font-weight: 700; }
.cfa-options input { flex-shrink: 0; accent-color: var(--vp-c-brand-1); }
.cr-input textarea { display: block; width: 100%; resize: vertical; padding: .75rem; border: 1px solid var(--vp-c-border); border-radius: 7px; color: var(--vp-c-text-1); background: var(--vp-c-bg); font: inherit; }
.cfa-actions { display: flex; gap: .75rem; margin: 1rem 0; }
.cfa-actions button { border-radius: 7px; padding: .65rem 1.1rem; background: var(--vp-button-brand-bg); color: var(--vp-button-brand-text); font-weight: 600; cursor: pointer; }
.cfa-actions button:disabled { opacity: .5; cursor: default; }
.cfa-actions .reset { color: var(--vp-c-text-1); background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-border); }
.cfa-analysis { border-top: 1px solid var(--vp-c-divider); padding-top: 1rem; }
.cfa-result { margin-bottom: 1rem; }
.cfa-options :deep(p) { margin: 0; }
.cfa-interactive :deep(h3) { margin-top: 1.5rem; }
button:focus-visible, textarea:focus-visible, input:focus-visible { outline: 2px solid var(--vp-c-brand-1); outline-offset: 3px; }
</style>
