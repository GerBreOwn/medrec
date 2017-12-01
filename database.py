import os

user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
host = 'postgres-bdr'
port = '5432'
engine = create_engine('postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, db))

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import doctor.models, patient.models, visit.models
    Base.metadata.create_all(bind=engine)
