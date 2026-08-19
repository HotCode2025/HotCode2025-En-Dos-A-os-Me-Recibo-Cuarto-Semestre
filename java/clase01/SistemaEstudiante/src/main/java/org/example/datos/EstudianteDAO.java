package org.example.datos;

import org.example.dominio.Estudiante;
import static  org.example.conexion.Conexion.getConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class EstudianteDAO {
    //Método listar
    public List<Estudiante> listar() {
        List<Estudiante> estudiantes = new ArrayList<>();
        //Creamos algunos objetos que son necesarios para comunicarnos con la base de datos
        PreparedStatement ps; //Envía la sentencia a la DB.
        ResultSet rs; //Obtenemos el resultado de la DB.
        //Creamos la conexión.
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2026";
        try {
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while (rs.next()) {
                var estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idestudiantes2026"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                //
                estudiantes.add(estudiante);
            }
        } catch (Exception e ){
            System.out.println("Ocurrió un error al seleccionar los estudiatnes" + e.getMessage());
        } finally {
            try {
                con.close();
            } catch (Exception e ) {
                System.out.print("Ocurrio un error al cerrar la conexión" + e);
            }
        }
        return estudiantes;
    }//fin método listar

    //incio método búscar por ID

    public boolean buscarEstudiantePorId(Estudiante estudiante) {
        PreparedStatement ps;
        ResultSet rs;
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2026 WHERE idestudiantes2026=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1, estudiante.getIdEstudiante());
            rs = ps.executeQuery();
            if (rs.next()) {
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                return true;
            }
        } catch (Exception e ){
            System.out.println("Ocurrió un error en la búsqueda" + e.getMessage());

        } finally {
            try {
                con.close();
            } catch (Exception e ) {
                System.out.print("Ocurrio un error al cerrar la conexión" + e);
            }
        }
        return false;
    }//fin método buscar estudiante

    //Agregar un estudiante
    public boolean agregarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "INSERT INTO estudiantes2026 (nombre, apellido, telefono, email) VALUES (?, ?, ?, ?)";
        try{
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.execute();
            return true;
        } catch(Exception e){
            System.out.println("Ocurrió un error al agregar estudiante: " + e.getMessage());
        } finally {
            try {
                con.close();
            } catch (Exception e ) {
                System.out.print("Ocurrio un error al cerrar la conexión" + e);
            }
        }
        return false;
    }//fin método agregar

    //Método para modificar estudiante
    public boolean modificarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "UPDATE estudiantes2026 SET nombre=?, apellido=?, telefono=?, email=? WHERE idestudiantes2026=?";
        try{
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.setInt(5, estudiante.getIdEstudiante());
            ps.execute();
            return true;
        } catch (Exception e){
            System.out.println("Error al modificar estudiante: " + e.getMessage());
        }finally {
            try {
                con.close();
            } catch (Exception e ) {
                System.out.print("Ocurrio un error al cerrar la conexión" + e);
            }
        }
        return false;
    }//fín método modificar estudiante

    public boolean eliminarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "DELETE FROM estudiantes2026 WHERE idestudiantes2026=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1, estudiante.getIdEstudiante());
            ps.execute();
            return true;
        } catch (Exception e){
            System.out.println("Error al eliminar estudiante: "+e.getMessage());
        }finally {
            try {
                con.close();
            } catch (Exception e ) {
                System.out.print("Ocurrio un error al cerrar la conexión" + e);
            }
        }
        return false;
    }

    public static void main(String[] args) {
        var estudiantesDao = new EstudianteDAO();

        //Modificar estudiante
        var estudianteModificado = new Estudiante(1, "Ramiro", "Muñoz", "1234654678", "rami@mail.com");
        var modificado = estudiantesDao.modificarEstudiante(estudianteModificado);
        if(modificado)
            System.out.println("Estudiante modificado: "+estudianteModificado);
        else
            System.out.println("No se modifico el estudiante: "+estudianteModificado);

        //Listar los estudiantes.
        List<Estudiante> estudiantes = estudiantesDao.listar();
        estudiantes.forEach(System.out::println);


        //Agregar estudiante
        /*
        var nuevoEstudiante = new Estudiante("Tomas", "Blanco", "254658745", "tomas@mail.com");
        var agregado = estudiantesDao.agregarEstudiante(nuevoEstudiante);
        if(agregado)
            System.out.println("Estudiante agregado: "+nuevoEstudiante);
        else
            System.out.println("No se ha agregado estudiante: "+nuevoEstudiante);
        */

        //Eliminar estudiante con id 3
        var estudianteEliminar = new Estudiante(3);
        var eliminado = estudiantesDao.eliminarEstudiante(estudianteEliminar);
        if(eliminado)
            System.out.println("Estudiante eliminado: "+estudianteEliminar);
        else
            System.out.println("No se elimino estudiante: "+estudianteEliminar);


        //Buscar por id
        var estudiante1 = new Estudiante(1);
        System.out.println("Estudiantes antes de la busqueda: "+estudiante1);
        var encontrado = estudiantesDao.buscarEstudiantePorId(estudiante1);
        if(encontrado)
            System.out.println("Estudiante encontrado: "+estudiante1);
        else
            System.out.println("No se encontro el estudiante: "+estudiante1.getIdEstudiante());
    }
}
