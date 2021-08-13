tinymce.init({
  selector: 'textarea.tinymce',
  setup: function (editor) {
    editor.on('change', function () {
        editor.save();
    });},
  height: 300,
  menubar: false,
  plugins: 'lists',
  toolbar: 'undo redo | bold italic underline | alignleft aligncenter alignright ' +
  'alignjustify | bullist numlist outdent indent | ' +
  'removeformat | help',
});
tinymce.init({
  selector: 'textarea.tinymce-sm',
  setup: function (editor) {
    editor.on('change', function () {
        editor.save();
    });},
  height: 200,
  menubar: false,
  toolbar: 'undo redo | bold italic underline | alignleft aligncenter alignright ' +
  'alignjustify | bullist numlist outdent indent | ' +
  'removeformat | help',
});
