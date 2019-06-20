<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Компот</title>
    <link rel="stylesheet" href="<?= get_template_directory_uri(); ?>/public/css/style.css">
    <link rel="stylesheet" href="<?= get_template_directory_uri(); ?>/socicon/css/styles.css">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">

    <?php wp_head(); ?>
</head>
<body>

<header>
    <a href="<?= site_url(); ?>"><img class="header__logo"
                                      src="<?= get_template_directory_uri(); ?>/public/img/kp-logo-155x128.png"
                                      alt="КОМПОТ"></a>
    <nav>
        <div class="navbar" id="myTopnav">
            <a href="<?= site_url(); ?>">ГОЛОВНА</a>
            <a href="<?= site_url('plans-and-payment'); ?>">ТАРИФИ ТА ОПЛАТА</a>
            <a href="<?= site_url('agreement'); ?>">ПУБЛІЧНИЙ ДОГОВІР</a>
            <a href="#contacts">КОНТАКТИ</a>
            <a href="https://kompot.uz.ua:9443/" target="_blank">ОСОБИСТИЙ КАБІНЕТ</a>
            <div class="dropdown">
                <a class="dropbtn icon" href="#" id="menu">&#9776;</a>
                <div class="dropdown-content">
                    <a href="<?= site_url(); ?>">ГОЛОВНА</a>
                    <a href="<?= site_url('plans-and-payment'); ?>">ТАРИФИ ТА ОПЛАТА</a>
                    <a href="<?= site_url('agreement'); ?>">ПУБЛІЧНИЙ ДОГОВІР</a>
                    <a href="#contacts">КОНТАКТИ</a>
                    <a href="https://kompot.uz.ua:9443/" target="_blank">ОСОБИСТИЙ КАБІНЕТ</a>

                </div>
            </div>
        </div>
    </nav>
</header>
