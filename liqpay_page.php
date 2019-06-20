<?php
/**
 * Template Name: LiqPay
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/#single-post
 *
 *
 */

include_once('LiqPay.php');

get_header();
?>
    <main>
        <div class="main__welcome">
            <h1>Інтернет провайдер <span class="mycompany">&laquo;КОМПОТ&raquo;</span></h1>
            <p>Сервіс кращий за ціну!</p>
        </div>
        <div class="main__team" style="margin-top: 0">

            <form method="POST" accept-charset="utf-8" action=" <?= get_template_directory_uri() ?>/liqpay/liqpay.py">

                <input type="hidden" id="check_user" name="action" value="confirm">
                <img class="aligncenter" src="//static.liqpay.ua/logo/liqpay5.png" name="btn_text" alt="liqpay">
                <br>
                <b>Сума платежу</b>
                <input type="number" id="liqpay_amount" min="1" max="900" step="1" size="3" maxlength="3" name="summ"
                       value="" placeholder="150" required="required"><b>грн.</b>
                <br>
                <br>
                <b> Логін абонента (LOGIN)</b>
                <input type="text" id="liqpay_description" size="20" maxlength="100" name="login" value=""
                       placeholder="" required="required">

                <input type="hidden" name="description" value="Послуга Інтернет">
                <input type="hidden" name="type" value="buy">
                <input type="hidden" name="pay_way" value="card,delayed">
                <input type="hidden" name="language" value="ua">
                <br>
                <br>
                <input class="aligncenter" type="image" src="//static.liqpay.ua/buttons/p1ru.radius.png" name="btn_text"
                       alt="pay">
                <br>
                До оплати приймаються карти будь-яких банків:


            </form>


        </div>
    </main>

<?php
get_footer();