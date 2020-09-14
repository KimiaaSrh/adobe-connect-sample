<template>
    <div id="add-blog">
        <h2>Create a New Meeting</h2>
        <form v-if="!submitted">
            <label>Meeting Topic:</label>
            <input type="text" v-model.lazy="blog.title" required />
            <label>Meeting Description:</label>
            <textarea v-model.lazy.trim="blog.content"></textarea>
            <div id="checkboxes">
                <p>Meeting Categories:</p>
                <label>Scientific</label>
                <input type="checkbox" value="Scientific" v-model="blog.categories" />
                <label>Home Decor</label>
                <input type="checkbox" value="Home Decor" v-model="blog.categories" />
                <label>Sports</label>
                <input type="checkbox" value="Sports" v-model="blog.categories" />
                <label>Social Economic</label>
                <input type="checkbox" value="Social Economic" v-model="blog.categories" />
            </div>
            <label>Start Date and Time:</label>
            <input type="date" id="start" name="trip-start" value="2020-07-22" min="2020-01-01" max="2020-12-31" v-model="blog.date">
            <select v-model="blog.time">
                <option value="0">12:00 am</option>
                <option value="1">1:00 am</option>
                <option value="2">2:00 am</option>
                <option value="3">3:00 am</option>
                <option value="4">4:00 am</option>
                <option value="5">5:00 am</option>
                <option value="6">6:00 am</option>
                <option value="7">7:00 am</option>
                <option value="8">8:00 am</option>
                <option value="9">9:00 am</option>
                <option value="10">10:00 am</option>
                <option value="11">11:00 am</option>
                <option value="12">12:00 pm</option>
                <option value="13">1:00 pm</option>
                <option value="14">2:00 pm</option>
                <option value="15">3:00 pm</option>
                <option value="16">4:00 pm</option>
                <option value="17">5:00 pm</option>
                <option value="18">6:00 pm</option>
                <option value="19">7:00 pm</option>
                <option value="20">8:00 pm</option>
                <option value="21">9:00 pm</option>
                <option value="22">10:00 pm</option>
                <option value="23">11:00 pm</option>
            </select>
            <hr>
            <button v-on:click.prevent="post" class="myButton">Add Meeting</button>
        </form>
        <div v-if="submitted">
            <h3>Thanks for adding your post</h3>
        </div>
        <div id="preview">
            <h3>Preview Meeting Info</h3>
            <p>Meeting title: {{ blog.title }}</p>
            <p>Meeting content:</p>
            <p style="white-space: pre">{{ blog.content }}</p>
            <p>Meeting Categories:</p>
            <ul>
                <li v-for="category in blog.categories">{{ category }}</li>
            </ul>
            <p>Meeting date and time: {{ blog.date }} , {{ blog.time }} </p>
        </div>
        
    </div>
</template>

<script>
// Imports
import axios from 'axios';
import { TokenService } from '../storage/service';

export default {
    data () {
        return {
            blog: {
                title: '',
                content: '',
                categories: [],
                author: '',
                date:'',
                time:''
            },
            authors: ['The Net Ninja', 'The Angular Avenger', 'The Vue Vindicator'],
            submitted: false
        }
    },
    methods: {
        post: function(){
            // console.log(this.token);
            var postData = {
                // duration=models.DurationField()#7
                title: this.blog.title,
                description: this.blog.content,
                url: 'https://www.instagram.com/',
                category: this.blog.categories[0],
                startDate: this.blog.date,
                startTime: this.blog.time,
                passwordOftheMeeting: '',
                extraField: '',
                members: '',
                duration:'0:00[:00[.007980]]',
            };
            let axiosConfig = {
                headers: {
                'Authorization': 'Token ' + this.token
                }
            };
            axios.post(`http://127.0.0.1:8000/api/meeting/${postData.id}/create_meeting/`, postData,axiosConfig)
            .then(res => console.log('doroste'))
            .catch(err => console.log('ghalate'))
        }
    },
    created() {
        let token;
        this.token = TokenService.getToken();
  }
}
</script>

<style>
#add-blog *{
    box-sizing: border-box;
}
#add-blog{
    margin: 20px auto;
    max-width: 500px;
}
label{
    display: block;
    margin: 20px 0 10px;
}
input[type="text"], textarea{
    display: block;
    width: 100%;
    padding: 8px;
}
#preview{
    padding: 10px 20px;
    border: 1px dotted #ccc;
    margin: 30px 0;
}
h3{
    margin-top: 10px;
}
#checkboxes input{
    display: inline-block;
    margin-right: 10px;
}
#checkboxes label{
    display: inline-block;
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