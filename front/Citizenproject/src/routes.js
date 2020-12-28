import VueRouter from 'vue-router'
import Home from './pages/Home'
import News from './pages/News'
import MainSidebar from "./components/MainSidebar";
import ChildSidebar from "./components/ChildSidebar";
import Projects from "./pages/Projects";
import New from "./pages/New";
import Project from "./pages/Project";
import Docs from "./pages/Docs";
import Activities from "./pages/Activities";
import Sub_category from "./pages/Sub_category";
import CategoryItems from "./pages/CategoryItems";

export default new VueRouter({
  routes: [
    {
      path: '',
      components: {
        sidebar: MainSidebar,
        content: Home
      }
    },
    {
      path: '/news',
      components: {
        sidebar: ChildSidebar,
        content: News
      },
      meta: { isLongStyle: true, title: "Новости"  }
    },
    {
      path: '/new/:id',
      components: {
        sidebar: ChildSidebar,
        content: New
      },
      meta: { isLongStyle: true, title: "Новости"  }
    },
    {
      path: '/projects',
      components: {
        sidebar: ChildSidebar,
        content: Projects
      },
      meta: { title: "Проекты"  }
    },
    {
      path: '/category/:id',
      components: {
        sidebar: ChildSidebar,
        content: Sub_category
      },
      meta: { title: "Проекты", isLongStyle: true, }
    },
    {
      path: '/item/:id',
      components: {
        sidebar: ChildSidebar,
        content: CategoryItems
      },
      meta: { isLongStyle: true, title: "Проекты"  }
    },
    {
      path: '/projects/:id',
      components: {
        sidebar: ChildSidebar,
        content: Project
      },
      meta: { isLongStyle: true, title: "Проекты" }
    },
    {
      path: '/docs',
      components: {
        sidebar: ChildSidebar,
        content: Docs
      },
      meta: { isLongStyle: true, title: "Документы" }
    },
    {
      path: '/activities',
      components: {
        sidebar: ChildSidebar,
        content: Activities
      },
      meta: { isLongStyle: true, title: "Деятельность"  }
    },
    {
      path: '*',
      components: {
        sidebar: MainSidebar,
        content: Home
      }
    },
  ],
  mode: 'history',
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    if (to.hash) {
      return { selector: to.hash }
    }
    return {x: 0, y: 0}
  }
})
