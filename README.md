# FoxLink-PY
Per lanciare l'applicazione bisogna prima far partire l'agente docker

Poi far partire la network isolata di comunicazione contenente mongodb, searx, kafka e zookeeper tramite

    start_environment.sh
Attendere quanche secondo, dopodichè lanciate l'applicazione con

    start_application.sh
    
Per stoppare l'applicazione:

    stop_application.sh
    
Per stoppare la network isolata di comunicazione:

    stop_environment_network.sh
    
Per cancellare i container dell'applicazione:

    delete_application.sh
    
Per cancellare i container della network isolata di comunicazione:

    delete_environment.sh
