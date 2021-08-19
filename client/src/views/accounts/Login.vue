<template>
  <div>
    <h1>Login</h1>
    <!-- 로그인 정보 입력 페이지 -->
    <div>
      <label for="username">사용자 이름: </label> 
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <button @click="login">로그인</button>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return { // 받을 credential 데이터 설정
      credentials: {
        username: null,
        passwords: null,
      }
    }
  },
  methods: {
    login: function () { // login 함수 설정
      axios({ // post 방식으로 backend에 credential 데이터로 요청 보냄
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => { // token 저장 및 login 후 Main 페이지로 이동
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Main'})
          this.isLogin = true
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
