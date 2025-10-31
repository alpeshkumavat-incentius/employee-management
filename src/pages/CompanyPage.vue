<template>
  <div>
    <q-card>
      <q-select
        standout="bg-teal text-white"
        v-model="show"
        :options="options"
        label="Select Designation"
        v-on:update:modelValue="updateDesignation()"
        
      />
    </q-card>

    <div>
      <q-dialog v-model="display" persistent >
        <q-card>
          <q-card-section class="row items-center">
            <span class="q-ml-sm">you selected !!</span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="Ok" color="primary" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
export default {
  setup() {
    return {
      show: ref(''),
      display: ref(false),
      options: ['Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'],
    }
  },
  methods: {
    updateDesignation() {
      this.display = true;
    },
  },
}
</script>
