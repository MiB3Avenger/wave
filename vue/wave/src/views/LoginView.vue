<script>
export default {
    methods: {
        switchLogin () {
            if (this.flag) {
                document.querySelector('.pre-box').style.transform = "translateX(100%)";
                document.querySelector('.pre-box').style.backgroundColor = "#c9e0ed";
            } else {
                document.querySelector('.pre-box').style.transform = "translateX(0%)";
                document.querySelector('.pre-box').style.backgroundColor = "#edd4dc";
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
                        <FormKit type="text" name="username" label="Username" />
                        <FormKit type="text" name="email" label="Email" />
                        <FormKit type="password" name="password" label="Password"/>
                        <FormKit type="password" name="confirmPassword" label="Confirm Password" />
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
                        <FormKit type="text" name="username" label="Username" />
                        <FormKit type="password" name="password" label="Password"/>
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
span {
    position: absolute;
    z-index: 0;
    bottom: 0;
    background-color: radial-gradient(circle at 72% 28%, #fff 3px, #ff7edf 8%, #5b5b5b, #aad7f9 100%);
    box-shadow: inset 0 0 6px #fff,
                inset 3px 0 6px #eaf5fc,
                inset 2px -2px 10px #efcde6,
                inset 0 0 60px #f9f6de,
                0 0 20px #fff
                ;
    border-radius: 50%;
    animation: myMove 4s linear infinite;
    transition: 2s;
}

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
    border: 1px solid rgba(255,255,255,.6);
    box-shadow: 2px 1px 19px rgba(0, 0, 0, .1);
}

.pre-box {
    width: 50%;
    height: 100%;
    position: absolute;
    left: 0;
    top: 0;
    z-index: 99;
    border-radius: 4px;
    background-color: #edd4dc;
    box-shadow: 2px 1px 19px rgba(0, 0, 0, .1);
    transition: 0.5s ease-in-out;

    h1 {
        margin-top: 150px;
        text-align: center;
        letter-spacing: 5px;
        text-shadow: 4px 4px 3px rgba(0, 0, 0, .1);
        color: var(--color-heading);
    }

    p {
        height: 30px;
        line-height: 30px;
        text-align: center;
        margin: 20px 0;
        font-weight: bold;
        user-select: none;
        text-shadow: 4px 4px 3px rgba(0, 0, 0, .1);
        color: var(--color-heading);
    }
}

.img-box {
    width: 200px;
    height: 200px;
    margin: 20px auto;
    border-radius: 50%;
    overflow: hidden;
    user-select: none;
    box-shadow: 4px 4px 3px rgba(0, 0, 0, .1);

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
        letter-spacing: 5px;
        user-select: none;
    }
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
            border-bottom: 1px solid white;
        }
    }
}
</style>