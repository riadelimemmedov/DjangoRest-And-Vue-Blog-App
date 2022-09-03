<template>
  <div class="hello">
    <picture-input
      ref="pictureInput"
      width="600"
      height="600"
      margin="16"
      accept="image/jpeg,image/png,image/jpg"
      size="5000"
      radius="50"
      :removable="true"
      :hideChangeButton="false"
      button-class="btn"
      buttonClass="btn btn-primary button"
      removeButtonClass="btn btn-danger button"
      :custom-strings="{
        upload: '<h1>Bummer!</h1>',
        drag: 'Drag a 😺 GIF or GTFO'
      }"
      @change="onChange">
    </picture-input>

  </div>
</template>

<script>
    import PictureInput from 'vue-picture-input'

    export default {
      name: 'app',
      data () {
        return {
          image:''
        }
      },
      components: {
        PictureInput
      },
      methods: {
        onChange (image) {
          console.log('New picture selected!')
          if (image) {
            console.log('Picture loaded.')
            this.image = image
          } else {
            console.log('FileReader API not supported: use the <form>, Luke!')
          }
        }
      }
    }

</script>
