<template>
    <div id="show-blogs">
        <h1>All Meetings</h1>
        <div v-for="blog in blogs" class="single-blog">
            <h4>Title : {{ blog.title }}</h4>
            <h5>Organizer  : {{ blog.organizer }}</h5>
            <h6>Meeting Categories  : {{ blog.category }}</h6>
            <hr>
            <h5>Short Description : {{ blog.description }}</h5>
            <p>Start Date  : {{ blog.startDate }} , Start Time: {{ blog.startTime }}</p>
            <p>Duration  : {{ blog.duration }}</p>
            <!-- <p>Members  : {{ blog.members_list }}</p> -->
            <!-- {{blog}} -->
            <button class="myButton" v-on:click="addToJoin(blog)">
                <router-link to="/meating" exact>Meeting Page</router-link>
            </button>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { TokenService } from '../storage/service';

export default {
    props: {
        blog: {}
    },
    data () {
        return {
            blogs: []
        }
    },
    methods: {
        printt:function(){
            console.log("sag");
            console.log(this.blogs);
        },
        addToJoin:function(blog){
            this.token = TokenService.getToken()
            var postData = {
                meetingId: blog,
                extraField: '',
            };
            let axiosConfig = {
                headers: {
                'Authorization': 'Token ' + this.token
                }
            };
            axios.post(`http://127.0.0.1:8000/api/join/${blog.id}/create_joinToMeeting/`, postData,axiosConfig)
            .then(console.log('doroste karrrrrr'))
            .catch(console.log('ghalate karrrrrr'))
        }
    },
    created() {
        this.$http.get('http://127.0.0.1:8000/api/meeting/').then(function(data){
            this.blogs = data.body;
            console.log('hiii');
            // console.log(data);
        });
        let token;
        this.token = TokenService.getToken();
    }
}
</script>

<style>
#show-blogs{
    max-width: 800px;
    margin: 0px auto;
}
.single-blog{
    padding: 20px;
    margin: 20px 0;
    box-sizing: border-box;
    background: rgb(238, 212, 212);
}
.myButton {
	box-shadow:inset 0px 39px 0px -24px #d18d8a;
	background:linear-gradient(to bottom, #e4685d 5%, #eb675e 100%);
	background-color:#e4685d;
	border-radius:4px;
	border:1px solid #ffffff;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:15px;
	padding:6px 15px;
	text-decoration:none;
	text-shadow:0px 1px 0px #b23e35;
}
.myButton:hover {
	background:linear-gradient(to bottom, #eb675e 5%, #e4685d 100%);
	background-color:#eb675e;
}
.myButton:active {
	position:relative;
	top:1px;
}


</style>