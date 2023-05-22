<template>
  <div>
    <p>{{ movie.title }}</p>
  </div>
</template>

<script>
export default {
    name: 'MyLikesItem',
    props: {
        movie: Object
    }
}
</script>

<style>

</style>