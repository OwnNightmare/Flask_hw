import flask
from flask import request
from flask.views import MethodView
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = flask.Flask('app')
PG_DSN = 'postgresql://admin:1234@127.0.0.1:5432/advdb'
engine = create_engine(PG_DSN, encoding='utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class AdvModel(Base):
    __tablename__ = 'advertisements'
    id = Column(Integer, primary_key=True)
    head = Column(String(100), nullable=False)
    description = Column(String(350), nullable=False)
    owner = Column(String(50), nullable=False)
    create_date = Column(DateTime, server_default=func.now())


Base.metadata.create_all(engine)


class AdvView(MethodView):
    def get(self, adv_id):
        with Session() as session:
            selected_adv = session.query(AdvModel).filter_by(id=adv_id).first()
            adv_dict = {'id': selected_adv.id, 'head': selected_adv.head, 'description': selected_adv.description,
                        'owner': selected_adv.owner, 'create_date': selected_adv.create_date}
            print(flask.jsonify(adv_dict).content_encoding)
        return flask.jsonify(adv_dict)


    def post(self):
        new_adv_data = request.json
        with Session() as session:
            new_adv = AdvModel(head=new_adv_data['head'], description=new_adv_data['description'],
                               owner=new_adv_data['owner'])
            session.add(new_adv)
            session.commit()
            return flask.jsonify({'adv': new_adv.head})

    def delete(self):
        ...


app.add_url_rule('/adv/', view_func=AdvView.as_view('create_adv'), methods=['POST'])
app.add_url_rule('/adv/<int:adv_id>/', view_func=AdvView.as_view('get_adv'), methods=['GET'])

