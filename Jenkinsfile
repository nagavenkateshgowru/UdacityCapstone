pipeline {
   agent any

   stages {
      stage('clone') {
         steps {
            echo 'Hello World'
         }
      }
      stage('Clone Project') {
          steps {
            git url: 'https://github.com/nagavenkateshgowru/UdacityCapstone.git'
        }
      }
      stage('PyLint Test') {
         steps {
            sh 'pwd'
            sh 'ls'
            sh 'which python'
            sh 'env'
            sh 'pylint ./app/app.py'
         }
      }
      stage('Test Flask APP') {
         steps {
            sh 'pwd'
            sh 'env'
            sh 'export PYTHONPATH=$WORKSPACE'
            sh 'env'
            sh 'python ./test/test.py'
         }
      }
       stage('Build Image') {
         steps {
            sh 'echo ${USER}'
            sh 'docker build -t test:0.${BUILD_ID} .'
         }
      }
   }
}
