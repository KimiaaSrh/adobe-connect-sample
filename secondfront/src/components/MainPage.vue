<template>
    <div >
        <body class="back">
            <label for="" class="sag"> Are you Interested in Recieving Newspaper? :)) </label>
            <br>
             <!-- <label for="" class="sag">Enter your Email below</label> -->
             <br>
             <input type="text" name="" id="" placeholder="Enter your Email Here" class="sag">
        </body>
    </div>
</template>

<script>

export default {
  data () {
      return{
          
      }
    
  },
  methods:{
      
  }
}
</script>

<style scoped>
.back{
    background-image: url(../assets/bar.jpg);
    /* background-size: 100%;
    background-color: violet; */
    margin: auto 10px;
    width: auto;
    margin-left: 100px;
    height: 2000px;
    /* background-color: yellow; */
}
.sag{
    border-radius:4px;
    box-shadow:inset 0px 39px 0px -24px #dbc4c1;
    /* color: rgb(14, 13, 11); */
	background:linear-gradient(to bottom, #ca918c 5%, #cfa5a2 100%);
	background-color:#dbc4c1;
	border:1px solid #ffffff;
    width: 20%;
}
</style>
