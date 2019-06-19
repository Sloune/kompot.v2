<?php

/**
 * Template Name: Agreement
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
        <div class="wrapper">
            <?= $post->post_content; ?>
        </div>

    </main>


<?php get_footer();