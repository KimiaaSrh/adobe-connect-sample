<template>
    <div>
        <nav>
        <ul>
            <li><router-link to="/show" exact>Meeting List</router-link></li>
            <li><router-link to="/" exact>Main</router-link></li>
            <li><router-link to="/add" exact>Create a new Meeting</router-link></li>
            <li><router-link to="/reg" exact>Register</router-link></li>
            <li><router-link to="/login" exact>Login</router-link></li>
            <li><router-link to="/quiz" exact>Create Quiz</router-link></li>
            <!-- <li><router-link to="/meating" exact>Meeting Page</router-link></li> -->
            <li><router-link to="/listquiz" exact>Quiz List</router-link></li>
            <!-- <li><router-link to="/listques" exact>Question List</router-link></li> -->
        </ul>
        </nav>
        
    </div>
    
</template>

<script>
export default {}
</script>

<style scoped>
ul{
    list-style-type: none;
    text-align: center;
    margin: 0;
}
li{
    display: inline-block;
    margin: 0 10px;
}
a{
    color: #fff;
    text-decoration: none;
    padding: 6px 8px;
    border-radius: 10px;
}
nav{
    background: rgb(185, 105, 105);
    padding: 14px 0;
    margin-bottom: 40px;
}
.router-link-active{
    background: #eee;
    color: #444;
}
.column-half{
   margin: 0 12px 24px 12px;
   width: 576px;
   
   float: left;
}
</style>