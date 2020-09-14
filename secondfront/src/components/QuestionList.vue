<template>
    <div id="show-blogs">
        <h1>All Questions</h1>
        <div v-for="blog in blogs" class="single-blog">
            <h4>Q Number : {{ blog.qNumber }}</h4>
            <h5>Question  : {{ blog.sooratesoal }}</h5>
            <hr>
            <div v-if="blog.typeTest">
                <ol>
                    <li><input type="text"  > {{blog.valueOftheTestAnswers}} </li>
                    <li><input type="text"  >{{blog.numberOftheTestAnswers}} </li>
                    <li><input type="text"  >{{blog.extraField}} </li>
                </ol>
            </div>
            <label for="">Please Enter Yout Answer below: </label>
            <br>
            <textarea name="Text1" cols="60" rows="2" ></textarea>
        </div>
    </div>
    
</template>

<script>
export default {
    data () {
        return {
            blogs: []
        }
    },
    methods: {
        printt:function(){
            console.log("sag");
            console.log(this.blogs);
        }
    },
    created() {
        this.$http.get('http://127.0.0.1:8000/api/question/').then(function(data){
            this.blogs = data.body;
            console.log('quiz gerefte shod');
            // console.log(data);
        });
    }
}
</script>

<style scoped>
#show-blogs{
    max-width: 800px;
    margin: 0px auto;
}
.single-blog{
    padding: 20px;
    margin: 20px 0;
    box-sizing: border-box;
    background: #eee;
}
.myButton {
	box-shadow: 0px 0px 0px 2px #9fb4f2;
	background:linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
	background-color:#7892c2;
	border-radius:10px;
	border:1px solid #4e6096;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:19px;
	padding:2px 9px;
	text-decoration:none;
	text-shadow:0px 1px 0px #283966;
}
.myButton:hover {
	background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
	background-color:#476e9e;
}
.myButton:active {
	position:relative;
	top:1px;
}
</style>