<template>
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color:#ced6e0;margin-top:-22px">
    <a class="navbar-brand" href="/">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item"><!-- !Bura router-link yazmalinsan yaddsa saxla active classsida orde duzeldersen ele indi router-link tagi icincde deyil deye islemir -->
          <a class="nav-link" href="" active-class="active">Posts</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/" active-class="active">Categories</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Profile</a>
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
</template>

<script>
  export default{

  }
</script>

<style>

</style>


