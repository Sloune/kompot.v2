<?php

if ((isset($_POST['call-name'])) && (isset($_POST['phonenumber']) && $_POST['phonenumber'] != "")) {

    $to = 'kompot.uz.ua@gmail.com';
    $subject = 'Передзвоніть мені | КОМПОТ-контактна-форма';
    $message = '
Від: ' . $_POST['call-name'] . '
Телефон: ' . $_POST['phonenumber'] ;
    $headers = "Content-type: text/plain; charset=utf-8 \r\n";
    $headers .= "From: Компот <admin@kompot.uz.ua>\r\n";
    mail($to, $subject, $message, $headers);

    echo json_encode(array('status' => 'success'));
} else {
    echo json_encode(array('status' => 'error'));
}