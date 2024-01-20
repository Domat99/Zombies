/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zombiesgame;

import java.io.IOException;
import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

/**
 *
 * @author domat
 */
public class ZombiesGame extends Application {

    public static Stage stg;

    @Override
    public void start(Stage primaryStage) throws IOException {
        stg = primaryStage;
        stg.setResizable(true);
//        stg.setMaxHeight(900);
//        stg.setMaxWidth(1500);
        stg.centerOnScreen();

        Parent root1 = FXMLLoader.load(getClass().getResource("PlayScreen.fxml"));

        Scene scene1 = new Scene(root1);

        primaryStage.setTitle("Zombies Game");
//        primaryStage.getIcons().add(logo);
        primaryStage.setScene(scene1);
        primaryStage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }

}