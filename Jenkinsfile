pipeline {
    agent any
    environment {
        // Si Terraform requiere variables de entorno, puedes definirlas aquí
        TF_VAR_example = "valor_ejemplo"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Terraform Init') {
            steps {
                sh 'pwd'
            }
        }
        stage('Terraform Plan') {
            steps {
                sh 'pwd'
            }
        }
        stage('Terraform Apply') {
            steps {
                // Se recomienda confirmar manualmente en entornos de producción.
               // sh 'terraform apply -auto-approve'
               sh'git pull'
            }
        }
    }
    post {
        always {
            cleanWs() // Limpia el workspace después de ejecutar el pipeline.
        }
        failure {
            echo "Hubo un fallo en la ejecución del pipeline"
        }
    }
}
