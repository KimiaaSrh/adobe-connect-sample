<template>
    <div id="show-blogs">
        <div>
            <label>Quiz Topic:</label>
            <input type="text"  v-model="qzTitle"/>
            <br>
            <label>Start Date and Time:</label>
            <input type="date" id="start" name="trip-start" value="2020-07-22" min="2020-01-01" max="2020-12-31" v-model="qzStartDate">
            <select v-model="qzStartTime" >
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
            <br>
            <label>set duration of the quiz please:</label>
            <input type="text" v-model="qzDuration" />
            <hr>
        </div>
        <div v-for="item in qs" class="single-blog">
            <h2>{{ item.title }}</h2>
            <label>multiple choice test</label>
            <input type="checkbox" value="multiple choice test" v-model="item.typeTest" />
            <label>Detailed examination</label>
            <input type="checkbox" value="Detailed examination" v-model="item.typeEx" />
            <!-- <article>{{ item.body }}</article> -->
            <!-- <p> {{item.type}} </p> -->
            <br>
            <label for="">Please Enter the Question below: </label>
            <br>
            <textarea name="Text1" cols="80" rows="3" v-model="item.sooratesoal"></textarea>
            <div v-if="item.typeTest">
                <ol>
                    <li><input type="text" value="choice 1" v-model="item.valueOftheTestAnswers"></li>
                    <li><input type="text" value="choice 2" v-model="item.numberOftheTestAnswers"></li>
                    <li><input type="text" value="choice 3" v-model="item.extraField"></li>
                </ol>
                <label for="">Please Enter the True Answer below: </label>
                <br>
                <textarea name="Text1" cols="20" rows="1" v-model="item.trueAnswer"></textarea>
            </div>
            <div v-if="item.typeEx">
                <label for="">Please Enter the True Answer below: </label>
                <br>
                <textarea name="Text1" cols="80" rows="3" v-model="item.trueAnswer"></textarea>
            </div>
        </div>
        <!-- <button v-on:click="save">save</button> -->
        <button v-on:click="addQ" class="myButton">add question</button>
        <button v-on:click="addQuiz" class="myButton">add a quiz</button>
    </div>
</template>

<script>
// Imports
import axios from 'axios';
import { TokenService } from '../storage/service';

export default {
    data () {
        return {
            qzTitle:'',
            qzStartDate:'',
            qzStartTime:'',
            qzDuration:'',
            title:1,
            qs:[],
            submitted: false
        }
    },
    methods: {
        save:function(){
            // if(this.title!=1)
            console.log(this.qs);
            // this.qs.push(this.quiz);
            // this.quiz.title++;
            // this.qs.push(this.quiz);
        },
        addQ:function(){
            var postData = {
                qNumber: this.title,
                sooratesoal: '',
                numberOftheTestAnswers: '',
                valueOftheTestAnswers: '',
                trueAnswer: '',
                typeTest: '',
                typeEx: '',
                extraField: '',
            };
            postData.title=this.title++;
            if( this.qs.length!=0){
                console.log('hiiiii');
                var outData=this.qs.pop();
                let axiosConfig = {
                headers: {
                'Authorization': 'Token ' + this.token
                }
                };
                axios.post(`http://127.0.0.1:8000/api/question/${postData.id}/create_question/`, outData,axiosConfig)
                .then(res => console.log('doroste dare q add mikone'))
                .catch(err => console.log('ghalate dare q add mikone'))
                this.qs.push(outData);
                // axios.post(`http://127.0.0.1:8000/api/qq/${postData.id}/create_quizquestion/`, outData,axiosConfig)
                // .then(res => console.log('doroste dare qq add mikone'))
                // .catch(err => console.log('ghalate dare qq add mikone'))
            }
            this.qs.push(postData);
            console.log(this.qs);
        },
        addQuiz:function(){
            var postData = {
                duration:this.qzDuration,
                topic: this.qzTitle,
                questions: '',
                url: 'https://www.instagram.com/',
                idOftheQuiz: 0,
                startDate: this.qzStartDate,
                startTime: this.qzStartTime,
                extraField: '',
            };
            let axiosConfig = {
                headers: {
                'Authorization': 'Token ' + this.token
                }
            };
            axios.post(`http://127.0.0.1:8000/api/quiz/${postData.id}/create_quiz/`, postData,axiosConfig)
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