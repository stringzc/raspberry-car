#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    /* tcp套接字 */
    tcpSocket = new QTcpSocket(this);
    view = new QWebEngineView(this);
    view->resize(500, 382); // 设置窗口大小
    setWebview();

    connect(tcpSocket, SIGNAL(connected()),
            this, SLOT(connected()));
    connect(tcpSocket, SIGNAL(disconnected()),
            this, SLOT(disconnected()));
    connect(tcpSocket,
            SIGNAL(stateChanged(QAbstractSocket::SocketState)),
            this,
            SLOT(socketStateChange(QAbstractSocket::SocketState)));
    connect(tcpSocket, SIGNAL(readyRead()),
            this, SLOT(receiveMessages()));
}

MainWindow::~MainWindow()
{
    delete ui;
}
void MainWindow::setWebview(){
    view->page()->load(QUrl("http://192.168.43.230:8000/stream.mjpg"));
    view->show(); // 显示视图

}
void MainWindow::receiveMessages()
{
    QByteArray array = tcpSocket->readAll();
    QImage bmpBuf;
    bmpBuf.loadFromData(array);
    ui->label_3->setPixmap(QPixmap::fromImage(bmpBuf));
}
/* 连接 */
void MainWindow::on_pushButton_cnn_clicked()
{
    /* 如果连接状态还没有连接 */
    if (tcpSocket->state() != tcpSocket->ConnectedState) {
        /* 指定IP地址和端口连接 */
        /*tcpSocket->connectToHost(IPlist[comboBox->currentIndex()],
                spinBox->value());*/
        tcpSocket->connectToHost(ui->textEdit->toPlainText(),
                ui->spinBox->value());
    }

}
/* 已连接 */
void MainWindow::connected()
{
    /* 显示已经连接 */
    ui->textBrowser->append("已经连上服务端");

    /* 设置按钮与下拉列表框的状态 */
    ui->pushButton_cnn->setEnabled(false);
    ui->pushButton_discnn->setEnabled(true);
    //comboBox->setEnabled(false);
    ui->spinBox->setEnabled(false);
}

/* 已断开连接 */
void MainWindow::disconnected()
{
    /* 显示已经断开连接 */
    ui->textBrowser->append("已经断开服务端");

    /* 设置按钮与下拉列表框的状态  */
    ui->pushButton_discnn->setEnabled(false);
    ui->pushButton_cnn->setEnabled(true);
    //comboBox->setEnabled(true);
    ui->spinBox->setEnabled(true);
}

/* 发送消息 */
void MainWindow::sendMessages(QString str)
{
    if(NULL == tcpSocket)
        return;

    if(tcpSocket->state() == tcpSocket->ConnectedState) {
        /* 发送消息 */
        tcpSocket->write(str.toUtf8().data());
    }
}

/* 连接状态改变槽函数 */
void MainWindow::socketStateChange(QAbstractSocket::SocketState state)
{
    switch (state) {
    case QAbstractSocket::UnconnectedState:
        ui->textBrowser->append("scoket状态：UnconnectedState");
        break;
    case QAbstractSocket::ConnectedState:
        ui->textBrowser->append("scoket状态：ConnectedState");
        break;
    case QAbstractSocket::ConnectingState:
        ui->textBrowser->append("scoket状态：ConnectingState");
        break;
    case QAbstractSocket::HostLookupState:
        ui->textBrowser->append("scoket状态：HostLookupState");
        break;
    case QAbstractSocket::ClosingState:
        ui->textBrowser->append("scoket状态：ClosingState");
        break;
    case QAbstractSocket::ListeningState:
        ui->textBrowser->append("scoket状态：ListeningState");
        break;
    case QAbstractSocket::BoundState:
        ui->textBrowser->append("scoket状态：BoundState");
        break;
    default:
        break;
    }
}

void MainWindow::on_pushButton_discnn_clicked()
{
    /* 断开连接 */
    tcpSocket->disconnectFromHost();
    /* 关闭socket*/
    tcpSocket->close();
}

void MainWindow::on_pushButton_d_2_clicked()
{
    ui->textBrowser->clear();
}

void MainWindow::on_pushButton_w_pressed()
{
    sendMessages("w");
}

void MainWindow::on_pushButton_w_released()
{
    sendMessages("p");
}

void MainWindow::on_pushButton_d_pressed()
{
    sendMessages("wd");
}

void MainWindow::on_pushButton_d_released()
{
    sendMessages("p");
}

void MainWindow::on_pushButton_sd_pressed()
{
    sendMessages("sd");
}

void MainWindow::on_pushButton_sd_released()
{
    sendMessages("p");
}

void MainWindow::on_pushButton_a_pressed()
{
    sendMessages("wa");
}

void MainWindow::on_pushButton_a_released()
{
    sendMessages("p");
}

void MainWindow::on_pushButton_sa_pressed()
{
    sendMessages("sa");
}

void MainWindow::on_pushButton_sa_released()
{
    sendMessages("p");
}

void MainWindow::on_pushButton_s_pressed()
{
    sendMessages("s");
}

void MainWindow::on_pushButton_s_released()
{
    sendMessages("p");
}

void MainWindow::on_pushButton_p_clicked()
{
    sendMessages("p");
}
