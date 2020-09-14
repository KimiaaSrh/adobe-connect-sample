<template>
    <div >
        <body  dir="rtl">
		<table border="0" width="90%" align="center" cellspacing="8">
			<tr><td class="myClass" colspan="2" height="70px"> {{this.theChosenOne.title}} </td></tr>
			<tr><td class="myClass2" rowspan="2" width="150px">
                <ul v-for="user in users ">
                    <li> {{user}} </li>
                </ul> </td>
                <tr><td class="myClass3" height="400px">whiteBoard</td></tr>
		</table>
        <!-- <aside>
            <p>The Epcot center is a theme park at Walt Disney World Resort featuring exciting attractions, international pavilions, award-winning fireworks and seasonal special events.</p>
        </aside> -->
	</body>
        
    </div>
</template>

<script>
// Imports
export default {
    data () {
        return {
            blogs: [],
            joins:[],
            lastJoin:{},
            theChosenOne:{},
            users:[],
        }
    },
    methods: {
        
    },
    created() {
        this.$http.get('http://127.0.0.1:8000/api/meeting/').then(function(data){
            this.blogs = data.body;
            // console.log('hiii');
            // console.log(data);
        });
        this.$http.get('http://127.0.0.1:8000/api/join/').then(function(data){
            this.joins = data.body;
            this.lastJoin=this.joins[this.joins.length-1];
            console.log(this.lastJoin);
            for (let index = 0; index < this.blogs.length; index++) {
                if(this.blogs[index].id==this.lastJoin.meetingId){
                    // console.log(this.blogs[index].title);
                    this.theChosenOne=this.blogs[index];
                    // this.users.push(this.lastJoin.meetingMember);
                }  
            }
            for (let index = 0; index < this.blogs.length; index++) {
                if(this.blogs[index].id==this.lastJoin.meetingId){
                    for (let index2 = 0; index2 < this.joins.length; index2++) {
                        if(this.blogs[index].id==this.joins[index2].meetingId){
                            if(!(this.joins[index2].meetingMember in this.users ))
                                this.users.push(this.joins[index2].meetingMember);
                        }
                        
                    }
                }    
            }
            // console.log(data);
        });
    }
}
</script>

<style scoped>
.myClass
{
   background-color: rgb(189, 147, 147);
}
.myClass2
{
   background-color:rgb(156, 124, 124);
}
.myClass3
{
   background-color: rgb(238, 199, 199);
}
aside {
  width: 20%;
  height:200px;
  padding-left: 15px;
  margin-left: 15px;
  float: right;
  font-style: italic;
  background-color: lightgray;
}
</style>