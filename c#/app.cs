// Archivo: MainPage.xaml.cs

using Microsoft.Maui.Controls;

namespace MiAppMaui
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();

            var label = new Label
            {
                Text = "¡Hola, .NET MAUI!",
                FontSize = 24,
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.CenterAndExpand
            };

            Content = new StackLayout
            {
                Children = { label }
            };
        }
    }
}
