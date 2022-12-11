#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTcpServer>
#include <QTcpSocket>
#include <QNetworkInterface>
#include <QDebug>
#include <QWebEngineView>
QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT
private:
    /* 通信套接字 */
    QTcpSocket *tcpSocket;
    /* 发送消息 */
    void sendMessages(QString);
    QWebEngineView *view;
    void setWebview();
public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:

    void on_pushButton_cnn_clicked();

    /* 已连接 */
    void connected();

    /* 已断开连接 */
    void disconnected();


    /* 连接状态改变槽函数 */
    void socketStateChange(QAbstractSocket::SocketState);

    void receiveMessages();
    void on_pushButton_discnn_clicked();

    void on_pushButton_d_2_clicked();

    void on_pushButton_w_pressed();

    void on_pushButton_w_released();

    void on_pushButton_d_pressed();

    void on_pushButton_d_released();

    void on_pushButton_sd_pressed();

    void on_pushButton_sd_released();

    void on_pushButton_a_pressed();

    void on_pushButton_a_released();

    void on_pushButton_sa_pressed();

    void on_pushButton_sa_released();

    void on_pushButton_s_pressed();

    void on_pushButton_s_released();

    void on_pushButton_p_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
