package org.example;

import org.example.conexion.Conexion;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
       var conexion = Conexion.getConnection();
       if(conexion != null) {
           System.out.println("conexión existosa" + conexion);
       }else {
           System.out.println("la conexión falló");
       } //fin main
    }// fin clase
}