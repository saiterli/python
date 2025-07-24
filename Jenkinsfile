pipeline {
  agent any

  environment {
    VENV = 'venv'
  }

  stages {
    stage('Clone Repo') {
      steps {
        echo 'Cloning code from GitHub...'
        checkout scm
      }
    }

    stage('Setup Python') {
      steps {
        sh '''
          python3 -m venv $VENV
          . $VENV/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run Tests') {
      steps {
        sh '''
          . $VENV/bin/activate
          pytest --junitxml=results.xml || true
        '''
      }
    }

    stage('Publish Results') {
      steps {
        junit 'results.xml'
      }
    }
  }

  post {
    always {
      sh 'rm -rf $VENV'
    }
  }
}
