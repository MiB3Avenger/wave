import { describe, it, expect } from "vitest";

import { mount } from "@vue/test-utils";
import { createRouter, createWebHistory } from "vue-router";
import { routes } from "../../router/index";
import Sidebar from "../Sidebar.vue";

describe("Sidebar", () => {
  it("renders properly", () => {
    const router = createRouter({
        history: createWebHistory(import.meta.env.BASE_URL),
        routes,
        strict: false,
        sensitive: true,
        scrollBehavior(to, from, savedPosition) {
            if (savedPosition) {
                return savedPosition
            } else {
                return { top: 0 }
            }
        },
    });
    
    const wrapper = mount(Sidebar, {
        global: {
            plugins: [router]
        }
    });
    expect(wrapper.html()).toContain("Home");
    expect(wrapper.html()).toContain("Search");
    expect(wrapper.html()).toContain("Notifications");
    expect(wrapper.html()).toContain("Create");
    expect(wrapper.html()).toContain("Profile");
    expect(wrapper.html()).toContain("Logout");
  });
});
