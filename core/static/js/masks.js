$(document).ready(function () {
    $("#id_contact_phone").inputmask("(99) 99999-9999", {removeMaskOnSubmit: true});
    $("#id_cpf").inputmask("999.999.999-99", {removeMaskOnSubmit: true});
    $("#id_birth_data").inputmask("99/99/9999");
});