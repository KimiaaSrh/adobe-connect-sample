<template>
  <header>
      <h1 v-on:click="changeTitle">{{ title }}</h1>
  </header>
</template>

<script>

import {bus} from '../main';

export default {
  props: {
      title: {
        type: String,
        required: true
      }
    },
  data () {
    return {
      
    }
  },
    methods: {
      changeTitle: function(){
        // this.$emit('changeTitleEvent', 'title e taghir yafte');
        this.title='title e taghir yafte';
        bus.$emit('titleChanged','title e taghir yafte');
      }
    }
}
</script>

<style scoped>
header{
    background-color: greenyellow;
    padding: 10px;
}
h1{
    color: indigo;
    text-align: center;
}
</style>
