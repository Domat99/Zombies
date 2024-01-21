/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zombies;

import java.awt.event.MouseEvent;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.SplitPane;
import javafx.scene.image.ImageView;
import javafx.scene.layout.AnchorPane;

/**
 *
 * @author domat
 */
public class Controller {

    
    @FXML
    private Button exit_btn;
    
    @FXML
    void exit_btn_clicked(ActionEvent event) {
        System.exit(0);
    }
    
        @FXML
    private ImageView canada_map;


    @FXML
    private AnchorPane left_pane_home;

    @FXML
    private ImageView mexico_map;

    @FXML
    private AnchorPane right_pane_home;

    @FXML
    private SplitPane split_pane_home;

    @FXML
    private ImageView usa_map;


    
    
    
}
