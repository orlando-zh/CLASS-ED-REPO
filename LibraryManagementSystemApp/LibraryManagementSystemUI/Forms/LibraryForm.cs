using LibraryManagementSystemData;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace LibraryManagementSystemUI.Forms
{
    public partial class LibraryForm : Form
    {
        private List<Book> booksList;

        public LibraryForm()
        {
            InitializeComponent();

            booksList = new List<Book>();
        }

        private void addBookButton_Click(object sender, EventArgs e)
        {
            string name = nameTextBox.Text;
            string isbn = isbnTextBox.Text;
            string author = authorTextBox.Text;

            Author authorName = new Author();
            authorName.Name = author;

            Book book = new Book();
            book.Name = name;
            book.ISBN = isbn;
            book.Author = authorName;

            booksList.Add(book);
            allBooksListBox.Items.Add(book);

        }

        private void borrowBookButton_Click(object sender, EventArgs e)
        {
            if (allBooksListBox.SelectedItem is Book selectedBook)
            {
                selectedBook.BorrowBook();
                allBooksListBox.Items.Clear();
                allBooksListBox.Items.Add((Book)selectedBook);
            }
        }
    }
}
