# -*- coding: utf-8 -*-

from amazonsqs import SQS
amazon_sqs = SQS()

while 1:
    print "---------------------------"
    print "-     AmazonSQS           -"
    print "---------------------------"
    print "- [N] Nuevo               -"

    colas = amazon_sqs.get_all_queues()
    for index in range(len(colas)):
        print "- [%s] %s" % (index, colas[index].name)

    print "---------------------------"
    print "- [Q] Salir               -"
    print "---------------------------"

    action = raw_input("Seleccione una accion o cola: ").upper()

    if action == "Q":
        print "Bytez"
        exit(1)

    elif action == "N":
        queue_name = raw_input("Nombre del nuevo queue: ")
        queue_timeout = raw_input("Timeout del nuevo queue: ")
        try:
            amazon_sqs.create_queue(queue_name, queue_timeout)
        except:
            print "Error creando queue"

    else:
        try:
            cola = colas[int(action)].name
            amazon_sqs.set_queue(cola)
        except:
            print "Error al seleccionar la cola"
            exit()

        print "---------------------------"
        print "-        %s" % cola
        print "---------------------------"
        print "- [N] Nuevo mensaje       -"
        print "- [L] Leer mensajes       -"
        print "- [B] Borrar mensaje      -"
        print "---------------------------"
        print "- [I] Detalles de queue   -"
        print "- [V] Vaciar queue        -"
        print "- [D] Eliminar queue      -"
        print "---------------------------"
        print "- [Q] Salir               -"
        print "---------------------------"

        action = raw_input("Seleccione una acción: ").upper()

        # Nuevo mensaje
        if action == "N":
            data = raw_input("Escriba la data a enviar: ")
            try:
                amazon_sqs.write(data)
                print "Datos escritos: %s" % data
            except:
                print "Error escribiendo: %s" % data

        # Leer mensajes
        elif action == "L":
            mensajes = amazon_sqs.get_messages()
            print "%s mensajes en %s" % (len(mensajes), cola)
            for mensaje in mensajes:
                print "id: %s - mensaje: %s" % (mensaje.id, mensaje.get_body())

        # Vaciar queue
        elif action == "V":
            rondas = raw_input("Escriba el número de intentos (10 mensajes x "
                " intento): ")

            try:
                mensajes = amazon_sqs.count()
                print "%s mensajes a eliminar" % mensajes

                if mensajes > 0:
                    amazon_sqs.clear()
                    print "Queue limpio"

            except:
                print "Error limpiando"

        # Eliminar queue
        elif action == "D":
            confirmar = raw_input("¿Está seguro que desea eliminar la cola? "
                "[S/N]: ").upper()
            if confirmar == "S":
                try:
                    amazon_sqs.delete_queue()
                    print "Queue %s eliminado" % cola
                except:
                    print "Error eliminando %s" % cola

        else:
            print "Operación inválida"
