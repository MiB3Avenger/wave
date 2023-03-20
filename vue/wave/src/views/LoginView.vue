<script>
export default {
    methods: {
        switchLogin () {
            if (this.flag) {
                document.querySelector('.pre-box').style.transform = "translateX(100%)";
                document.querySelector('.pre-box').style.backgroundColor = "var(--color-primary)";
                document.querySelector('.pre-box').style.color = "var(--color-on-primary)";
            } else {
                document.querySelector('.pre-box').style.transform = "translateX(0%)";
                document.querySelector('.pre-box').style.backgroundColor = "var(--color-primary-container)";
                document.querySelector('.pre-box').style.color = "var(--color-on-primary-container)";
            }
            this.flag = !this.flag;
        }
    },
    data() {
        return {
            flag: true
        }
    }
}
</script>
<script setup>
import Guest from '../layouts/Guest.vue';
</script>
<template>
    <Guest>
        <div class="box">
            <div class="pre-box">
                <h1>Welcome to Wave</h1>
                <p>Login to access the awesome!</p>
            </div>
            <div class="form">
                <div class="register-form">
                    <div class="title-box">
                        <h1>Register</h1>
                    </div>
                    <FormKit type="form" submit-label="Register">
                        <FormKit :floating-label="true" type="text" name="username" label="Username" />
                        <FormKit :floating-label="true" type="text" name="email" label="Email" />
                        <FormKit :floating-label="true" type="password" name="password" label="Password"/>
                        <FormKit :floating-label="true" type="password" name="confirmPassword" label="Confirm Password" />
                    </FormKit>
                    <div class="btn-box">
                        <p @click="switchLogin()">Have an account? Login here!</p>
                    </div>
                </div>
    
                <div class="login-form">
                    <div class="title-box">
                        <h1>Login</h1>
                    </div>
                    <FormKit type="form" submit-label="Login">
                        <FormKit :floating-label="true" type="text" name="username" label="Username" />
                        <FormKit :floating-label="true" type="password" name="password" label="Password"/>
                    </FormKit>
                    <div class="btn-box">
                        <p @click="switchLogin()">Don't have an account? Register here!</p>
                    </div>
                </div>
            </div>
        </div>
    </Guest>
</template>
<style lang="scss">
@keyframes myMove{
    0% {
        transform: translateY(0%);
        opacity: 1;
    }

    50% {
        transform: translate(10%, -1000%);
    }

    75% {
        transform: translate(-20%, -1200%);
    }

    99%{
        opacity: .9;
    }

    100%{
        transform: translateY(-1800%) scale(1.5);
        opacity: 0;
    }
}

.box {
    z-index: 2;
    display: flex;
    width: 60%;
    margin: auto;
    border-radius: 8px;
    border: 1px solid var(--vt-c-divider-dark-1);
}

.pre-box {
    width: 50%;
    height: 100%;
    position: absolute;
    left: 0;
    top: 0;
    z-index: 99;
    border-radius: 4px;
    background-color: var(--color-primary-container);
    color: var(--color-on-primary-container);
    transition: 0.5s ease-in-out;

    h1 {
        margin-top: 150px;
        text-align: center;
        letter-spacing: 5px;
    }

    p {
        height: 30px;
        line-height: 30px;
        text-align: center;
        margin: 20px 0;
        font-weight: bold;
        user-select: none;
    }
}

.img-box {
    width: 200px;
    height: 200px;
    margin: 20px auto;
    border-radius: 50%;
    overflow: hidden;
    user-select: none;

    img {
        width: 100%;
        transition: 0.5s;
    }
}

.form {
    display: flex;
    width: 100%;
    justify-content: space-between;
}

.login-form, 
.register-form{
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex: 0 1 50%;
    padding: 2rem;
}

.title-box {
    h1 {
        text-align: center;
        user-select: none;
    }
    margin-bottom: 1rem;
}


.btn-box {
    display: flex;
    justify-content: center;
    p {
        height: 30px;
        line-height: 30px;
        font-size: 14px;
        user-select: none;
        &:hover {
            cursor: pointer;
            border-bottom: 1px solid var(--color-on-primary);
        }
    }
}
</style>