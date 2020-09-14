<template>
  <div>
    <!-- <showBlog></showBlog>
    <add-blog></add-blog>
    <keep-alive>
      <component v-bind:is="component"></component>
    </keep-alive>
    <button v-on:click="component='formOne'">Show form one </button>
    <button v-on:click="component='formTwo'">Show form two </button>
    <formHelper>
      <div slot="form-header">
                <h3>This is the title of a form</h3>
                <p>This is some info about the form</p>
            </div>
            <div slot="form-fields">
                <input type="text" placeholder="name" required />
                <input type="password" placeholder="password" required />
            </div>
            <div slot="form-controls">
                <button v-on:click="handleSubmit">Submit</button>
            </div>
    </formHelper>
    <app-header v-bind:title="title" v-on:changeTitleEvent="updateTitle($event)"></app-header>
    <mainpage v-bind:datas="datas"></mainpage>
    <app-footer v-bind:title="title"></app-footer> -->
    <Header2></Header2>
    <router-view></router-view>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import MainPage from './components/MainPage.vue';
import formHelper from './components/formHelper.vue';
import formOne from './components/formOne.vue';
import formTwo from './components/formTwo.vue';
import addBlog from './components/addBlog.vue';
import showBlog from './components/showBlogs.vue';
import Header2 from './components/Header2.vue';

export default {
  components:{
    'app-header':Header,
    'app-footer':Footer,
    'mainpage':MainPage,
    'formHelper':formHelper,
    'formOne':formOne,
    'formTwo':formTwo,
    'addBlog':addBlog,
    'showBlog':showBlog,
    'Header2':Header2,
  },
  data () {
    return {
      datas: [
                {name: 'Ryu', speciality: 'Vue Components', show: false},
                {name: 'Crystal', speciality: 'HTML Wizardry', show: false},
                {name: 'Hitoshi', speciality: 'Click Events', show: false},
                {name: 'Tango', speciality: 'Conditionals', show: false},
                {name: 'Kami', speciality: 'Webpack', show: false},
                {name: 'Yoshi', speciality: 'Data Diggin', show: false}
            ],
      title: 'title e ghabli',
      component:'',
    }
  },
  methods:{
    updateTitle:function(input){
      this.title=input;
    },
    handleSubmit: function(){
      alert('thanks for submitting');
    }
  }
}
</script>

<style scoped>

</style>
