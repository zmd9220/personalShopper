<template>
  <div>
    <h1>Signup</h1>
    <!-- 관리자 회원 가입 페이지 -->
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    </div>
    <button @click="signup(credentials)">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: { // 회원가입 시 필요 정보
        username: null,
        password: null,
        passwordConfirmation: null,
      }  
    }
  },
  methods: {
    signup: function () { // 회원 가입 함수 정의
      axios({ // post 방식으로 credential 데이터 전달
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(res => { // 회원 가입 시 로그인 페이지로 이동
          console.log(res)
          this.$router.push({ name: 'Login'})
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
