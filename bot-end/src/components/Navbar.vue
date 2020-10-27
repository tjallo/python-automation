<template>
  <div>
    <v-app-bar app clipped-left flat dark>
      <v-toolbar-title>
        <span class="first-word font uppercase">hey</span>
        <span class="second-word font uppercase">stackoverflow</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-navigation-drawer app flat dark>
      <v-list>
        <v-list-item class="px-2">
          <v-list-item-avatar>
            <v-img src="https://randomuser.me/api/portraits/men/11.jpg"></v-img>
          </v-list-item-avatar>

          <v-list-item-title>
            <span class="username">Username</span>
          </v-list-item-title>
        </v-list-item>
        <v-list-item
          v-for="item in navbarlist"
          :key="item.route"
          :to="item.route"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>{{ item.text }}</v-list-item-content>
        </v-list-item>
      </v-list>

      <template v-slot:append>
        <v-list>
          <v-list-item @click="logout()">
            <v-list-item-icon>
              <v-icon color="red">mdi-logout</v-icon>
            </v-list-item-icon>
            <v-list-item-content>Logout</v-list-item-content>
          </v-list-item>
        </v-list>
      </template>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  data: () => ({
    drawer: true,
    navbarlist: [
      { icon: "mdi-view-dashboard", text: "Dashboard", route: "/" },
      { icon: "mdi-video-3d", text: "Viewer", route: "/viewer" },
    ],
  }),
  created: function () {},
  methods: {},
};
</script>

<style>
.font {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}
.uppercase {
  text-transform: uppercase;
}
.first-word {
  font-weight: 400;
}
.second-word {
  font-weight: 200;
  color: grey;
}
.item-tile-icon {
  color: black;
}
.username {
  color: whitesmoke;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  font-weight: lighter;
  letter-spacing: 0.001em;
}
</style>