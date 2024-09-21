namespace LibraryManagementSystemUI.Forms
{
    partial class LibraryForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            titleLabel = new Label();
            booksListGroupBox = new GroupBox();
            allBooksListBox = new ListBox();
            bookDataGroupBox = new GroupBox();
            authorTextBox = new TextBox();
            autorLabel = new Label();
            isbnTextBox = new TextBox();
            isbnLabel = new Label();
            nameTextBox = new TextBox();
            nameLabel = new Label();
            managementGroupBox = new GroupBox();
            borrowBookButton = new Button();
            addBookButton = new Button();
            booksListGroupBox.SuspendLayout();
            bookDataGroupBox.SuspendLayout();
            managementGroupBox.SuspendLayout();
            SuspendLayout();
            // 
            // titleLabel
            // 
            titleLabel.AutoSize = true;
            titleLabel.Font = new Font("Segoe UI", 18F, FontStyle.Bold, GraphicsUnit.Point, 0);
            titleLabel.Location = new Point(281, 22);
            titleLabel.Name = "titleLabel";
            titleLabel.Size = new Size(382, 41);
            titleLabel.TabIndex = 0;
            titleLabel.Text = "Administración Biblioteca";
            // 
            // booksListGroupBox
            // 
            booksListGroupBox.Controls.Add(allBooksListBox);
            booksListGroupBox.Location = new Point(31, 84);
            booksListGroupBox.Name = "booksListGroupBox";
            booksListGroupBox.Size = new Size(421, 496);
            booksListGroupBox.TabIndex = 1;
            booksListGroupBox.TabStop = false;
            booksListGroupBox.Text = "Listado de Libros";
            // 
            // allBooksListBox
            // 
            allBooksListBox.FormattingEnabled = true;
            allBooksListBox.HorizontalScrollbar = true;
            allBooksListBox.ItemHeight = 31;
            allBooksListBox.Location = new Point(26, 54);
            allBooksListBox.Name = "allBooksListBox";
            allBooksListBox.Size = new Size(376, 407);
            allBooksListBox.TabIndex = 0;
            // 
            // bookDataGroupBox
            // 
            bookDataGroupBox.Controls.Add(authorTextBox);
            bookDataGroupBox.Controls.Add(autorLabel);
            bookDataGroupBox.Controls.Add(isbnTextBox);
            bookDataGroupBox.Controls.Add(isbnLabel);
            bookDataGroupBox.Controls.Add(nameTextBox);
            bookDataGroupBox.Controls.Add(nameLabel);
            bookDataGroupBox.Location = new Point(474, 84);
            bookDataGroupBox.Name = "bookDataGroupBox";
            bookDataGroupBox.Size = new Size(443, 353);
            bookDataGroupBox.TabIndex = 2;
            bookDataGroupBox.TabStop = false;
            bookDataGroupBox.Text = "Datos Libros";
            // 
            // authorTextBox
            // 
            authorTextBox.BorderStyle = BorderStyle.FixedSingle;
            authorTextBox.Location = new Point(21, 296);
            authorTextBox.Name = "authorTextBox";
            authorTextBox.Size = new Size(394, 38);
            authorTextBox.TabIndex = 5;
            // 
            // autorLabel
            // 
            autorLabel.AutoSize = true;
            autorLabel.Location = new Point(21, 253);
            autorLabel.Name = "autorLabel";
            autorLabel.Size = new Size(76, 31);
            autorLabel.TabIndex = 4;
            autorLabel.Text = "Autor";
            // 
            // isbnTextBox
            // 
            isbnTextBox.BorderStyle = BorderStyle.FixedSingle;
            isbnTextBox.Location = new Point(21, 199);
            isbnTextBox.Name = "isbnTextBox";
            isbnTextBox.Size = new Size(394, 38);
            isbnTextBox.TabIndex = 3;
            // 
            // isbnLabel
            // 
            isbnLabel.AutoSize = true;
            isbnLabel.Location = new Point(21, 156);
            isbnLabel.Name = "isbnLabel";
            isbnLabel.Size = new Size(67, 31);
            isbnLabel.TabIndex = 2;
            isbnLabel.Text = "ISBN";
            // 
            // nameTextBox
            // 
            nameTextBox.BorderStyle = BorderStyle.FixedSingle;
            nameTextBox.Location = new Point(21, 91);
            nameTextBox.Name = "nameTextBox";
            nameTextBox.Size = new Size(394, 38);
            nameTextBox.TabIndex = 1;
            // 
            // nameLabel
            // 
            nameLabel.AutoSize = true;
            nameLabel.Location = new Point(21, 48);
            nameLabel.Name = "nameLabel";
            nameLabel.Size = new Size(203, 31);
            nameLabel.TabIndex = 0;
            nameLabel.Text = "Nombre del Libro";
            // 
            // managementGroupBox
            // 
            managementGroupBox.Controls.Add(borrowBookButton);
            managementGroupBox.Controls.Add(addBookButton);
            managementGroupBox.Location = new Point(474, 482);
            managementGroupBox.Name = "managementGroupBox";
            managementGroupBox.Size = new Size(443, 98);
            managementGroupBox.TabIndex = 3;
            managementGroupBox.TabStop = false;
            managementGroupBox.Text = "Administración";
            // 
            // borrowBookButton
            // 
            borrowBookButton.Location = new Point(170, 47);
            borrowBookButton.Name = "borrowBookButton";
            borrowBookButton.Size = new Size(118, 45);
            borrowBookButton.TabIndex = 1;
            borrowBookButton.Text = "Prestar";
            borrowBookButton.UseVisualStyleBackColor = true;
            borrowBookButton.Click += borrowBookButton_Click;
            // 
            // addBookButton
            // 
            addBookButton.Location = new Point(24, 47);
            addBookButton.Name = "addBookButton";
            addBookButton.Size = new Size(118, 45);
            addBookButton.TabIndex = 0;
            addBookButton.Text = "Agregar";
            addBookButton.UseVisualStyleBackColor = true;
            addBookButton.Click += addBookButton_Click;
            // 
            // LibraryForm
            // 
            AutoScaleDimensions = new SizeF(14F, 31F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(949, 592);
            Controls.Add(managementGroupBox);
            Controls.Add(bookDataGroupBox);
            Controls.Add(booksListGroupBox);
            Controls.Add(titleLabel);
            Font = new Font("Segoe UI", 13.8F, FontStyle.Bold, GraphicsUnit.Point, 0);
            Margin = new Padding(5);
            Name = "LibraryForm";
            Text = "LibraryForm";
            booksListGroupBox.ResumeLayout(false);
            bookDataGroupBox.ResumeLayout(false);
            bookDataGroupBox.PerformLayout();
            managementGroupBox.ResumeLayout(false);
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label titleLabel;
        private GroupBox booksListGroupBox;
        private ListBox allBooksListBox;
        private GroupBox bookDataGroupBox;
        private TextBox nameTextBox;
        private Label nameLabel;
        private TextBox isbnTextBox;
        private Label isbnLabel;
        private TextBox authorTextBox;
        private Label autorLabel;
        private GroupBox managementGroupBox;
        private Button addBookButton;
        private Button borrowBookButton;
    }
}