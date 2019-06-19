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
<!---->
<!--            <div class="b-main__sections-item" style="width:224px;">-->
<!--                <a href="http://www.kompot.uz.ua/" class="b-main__sections-button">Оплата онлайн</a>-->
<!--                <center><form method="POST" accept-charset="utf-8" action="http://kompot.uz.ua/liqpay/liqpay.py">-->
<!--                        <input type="hidden" id="check_user" name="action" value="confirm">-->
<!--                        <b></b> &nbsp;<br>-->
<!--                        <img src="//static.liqpay.ua/logo/liqpay5.png" name="btn_text">-->
<!--                        <b></b> &nbsp;<br>-->
<!--                        <b></b> &nbsp;<br>-->
<!--                        <b>Сума платежу</b> &nbsp;<input type="number" id="liqpay_amount" min="1" max="900" step="1" size="3" maxlength="3" name="summ" value="" placeholder="150" required="required">&nbsp;<b>грн.</b><br><br>-->
<!--                        <b>Логін абонента (LOGIN)</b>&nbsp;<input type="text" id="liqpay_description" size="20" maxlength="100" name="login" value="" placeholder="" required="required">&nbsp;<br>-->
<!---->
<!--                        <input type="hidden" name="description" value="Послуга Інтернет">-->
<!--                        <input type="hidden" name="type" value="buy">-->
<!--                        <input type="hidden" name="pay_way" value="card,delayed">-->
<!--                        <input type="hidden" name="language" value="ua">-->
<!--                        <br>-->
<!---->
<!--                        <p align="center" class="blinking" style="color: red;"><font size="3" ><b>Увага!<br />-->
<!--                                    З 5-го березня змінено тарифи!</b></font></p>-->
<!--                        <p align="center" ><font size="2" >-->
<!--                                Багатоповерхівки - 150 грн./міс. (Швидкість 100 мбіт), <br />-->
<!--                                Приватний сектор - 200 грн./міс. (Швидкість 50 мбіт)-->
<!---->
<!--                            </font></p>-->
<!---->
<!--                        <input type=image src="//static.liqpay.ua/buttons/p1ru.radius.png" name="btn_text">-->
<!--                    </form>-->
<!--                    <br>-->
<!--                    До оплати приймаються карти будь-яких банків:-->
<!--                </center>-->
<!--            </div>-->

        </div>
    </main>

<?php
get_footer();