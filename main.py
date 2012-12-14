# -*- coding: utf-8 -*-
import logging
import sys

from amazonsqs import SQS, log

amazon_sqs = SQS()
log.setup('INFO')


while 1:
    print "---------------------------"
    print "-     Amazon SQS Tool     -"
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
        logging.info("Bytez")
        exit(1)

    elif action == "N":
        queue_name = raw_input("Nombre del nuevo queue: ")
        queue_timeout = raw_input("Timeout del nuevo queue: ")
        try:
            amazon_sqs.create_queue(queue_name, queue_timeout)
        except:
            print >> sys.stderr, ("Error creando queue")

    else:
        try:
            cola = colas[int(action)].name
            amazon_sqs.set_queue(cola)
        except:
            print >> sys.stderr, ("Error al seleccionar la cola")
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
                logging.info("Datos escritos: %s" % data)
            except:
                print >> sys.stderr, ("Error escribiendo: %s" % data)

        # Leer mensajes
        elif action == "L":
            mensajes = amazon_sqs.get_messages()
            logging.info("%s mensajes en %s" % (len(mensajes), cola))
            for mensaje in mensajes:
                logging.info("id: %s - mensaje: %s" % (mensaje.id,
                    mensaje.get_body()))

        # Informacion queue
        elif action == "I":
            attributes = amazon_sqs.get_queue_attributes()
            for attribute in attributes.keys():
                logging.info("%s -> %s" % (attribute, attributes[attribute]))

        # Vaciar queue
        elif action == "V":
            rondas = raw_input("Escriba el número de intentos (10 mensajes x "
                " intento): ")

            try:
                mensajes = amazon_sqs.count()
                logging.info("%s mensajes a eliminar" % mensajes)

                if mensajes > 0:
                    amazon_sqs.clear()
                    logging.info("Queue limpio")

            except:
                print >> sys.stderr, ("Error limpiando")

        # Eliminar queue
        elif action == "D":
            confirmar = raw_input("¿Está seguro que desea eliminar la cola? "
                "[S/N]: ").upper()
            if confirmar == "S":
                try:
                    amazon_sqs.delete_queue()
                    logging.info("Queue %s eliminado" % cola)
                except:
                    print >> sys.stderr, ("Error eliminando %s" % cola)

        else:
            print "Operación inválida"
