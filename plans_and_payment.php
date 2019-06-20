<?php

/**
 * Template Name: Plans and Payment
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/#single-post
 *
 *
 */

get_header();
?>

    <main>
        <div class="main__welcome">
            <h1>Інтернет провайдер <span class="mycompany">&laquo;КОМПОТ&raquo;</span></h1>
            <p>Сервіс кращий за ціну!</p>
        </div>
        <h1 class="aligncenter">Тарифи на Інтернет</h1>
        <?= do_shortcode('[easy-pricing-table id="16"]'); ?>
        <h1 class="aligncenter">Тарифи на IPTV</h1>
        <?= do_shortcode('[easy-pricing-table id="18"]'); ?>
        <h2 class="aligncenter" style="text-align: center">Список усіх телеканалів ви зможете переглянути на сайті <a class="link"
                                                                                           href="https://omegatv.org/tariffs.html"
                                                                                           target="_blank">Omega TV</a>
        </h2>
        <div class="wrapper">
            <div class="plans">
                <div class="plan">
                    <img src="<?= get_template_directory_uri(); ?>/public/img/liqpay.png" alt="liqpay">
                    <h3>Liqpay</h3>
                    <p>Оплата онлайн</p>
                    <a href="<?= get_template_directory_uri(); ?>/pay" target="_blank"
                       class="btn btn-primary aligncenter" style="max-width: 200px">Детальніше</a>
                </div>
                <div class="plan">
                    <img src="<?= get_template_directory_uri(); ?>/public/img/easy_pay.png" alt="easy_pay">
                    <h3>Easy Pay</h3>
                    <p>Оплата онлайн</p>
                    <a href="https://easypay.ua/catalog/internet/kom-pot-internet" target="_blank"
                       class="btn btn-primary aligncenter" style="max-width: 200px">Детальніше</a>
                </div>
                <div class="plan">
                    <img src="<?= get_template_directory_uri(); ?>/public/img/privat24.jpg" alt="privat24">
                    <h3>Приват 24</h3>
                    <p>Оплата онлайн</p>
                    <a href="<?= get_template_directory_uri(); ?>/public/img/A4_qrpay_1.pdf" target="_blank"
                       class="btn btn-primary aligncenter" style="max-width: 200px">Детальніше</a>
                </div>
            </div>
        </div>
    </main>


<?php get_footer();