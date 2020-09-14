import addBlog from './components/addBlog.vue';
import showBlogs from './components/showBlogs.vue';
import Register from './components/Register.vue';
import Login from './components/Login.vue';
import Quiz from './components/Quiz.vue';
import MeatingPage from './components/MeatingPage.vue';
import MainPage from './components/MainPage.vue';
import QuizList from './components/QuizList.vue';
import QuestionList from './components/QuestionList.vue';

export default [
    { path: '/', component: MainPage},
    { path: '/show', component: showBlogs},
    { path: '/add', component: addBlog},
    { path: '/reg', component: Register},
    { path: '/login', component: Login},
    { path: '/quiz', component: Quiz},
    { path: '/meating', component: MeatingPage},
    { path: '/listquiz', component: QuizList},
    { path: '/listques', component: QuestionList}
]