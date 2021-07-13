import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import InitialPage from "./stages/InitialPage";
import ScoringPage from "./stages/ScoringPage";
import AnalysisPage from "./stages/AnalysisPage";
import BuildPage from "./stages/BuildPage";
import CitationPage from "./stages/CitationPage";
import LogisticsPage from "./stages/LogisticsPage";

Vue.config.productionTip = false

Vue.use(Router)
const router = new Router({
    routes: [
        {
            path: '/',
            name: 'Ibis - Genetic Circuit Scoring Algorithm',
            component: InitialPage,
        },
        {
            path: '/scoring',
            name: 'Ibis - Genetic Circuit Scoring Algorithm',
            component: ScoringPage,
        },
        {
            path: '/analysis',
            name: 'Ibis - Genetic Circuit Scoring Algorithm',
            component: AnalysisPage,
        },
        {
            path: '/build',
            name: 'Ibis - Genetic Circuit Scoring Algorithm',
            component: BuildPage,
        },
        {
            path: '/citation',
            name: 'Ibis - Genetic Circuit Scoring Algorithm',
            component: CitationPage,
        },
        {
            path: '/logistics',
            name: 'Ibis - Genetic Circuit Scoring Algorithm',
            component: LogisticsPage,
        },
    ]
})

new Vue({
    el: '#app',
    vuetify,
    render: h => h(App),
    router,
}).$mount('#app')
