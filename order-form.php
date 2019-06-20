<?php

if ((isset($_POST['call-name'])) && (isset($_POST['phone']) && $_POST['phone'] != "")) {
    $to = 'kompot.uz.ua@gmail.com';
    $subject = 'Замовлення на підключення по '.$_POST['street'].' вiд '.$_POST['call-name'].' | КОМПОТ-контактна-форма';
    $message = '
Від: ' . $_POST['call-name'] . "<br>".'
Email: ' . $_POST['email'] . "<br>".'
Телефон: ' . $_POST['phone'] . "<br><hr>".'
Вул: ' . $_POST['street'] . "<br>".'
Буд №: ' . $_POST['number'] . "<br>".'
Квартира №: ' . $_POST['app'] . "<br><hr>".$_POST['message'];
    $headers = "Content-type: text/html; charset=utf-8 \r\n";
    $headers .= "From: Компот <admin@kompot.uz.ua>\r\n";
    mail($to, $subject, $message, $headers);

    echo json_encode(array('status' => 'success'));
} else {
    echo json_encode(array('status' => 'error'));
}